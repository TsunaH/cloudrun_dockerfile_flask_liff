import liff from "@line/liff";

/**
 * 画面を開いたときの初期処理
 * 
 * @returns LINEのユーザID
 */
export async function getLineId() {
  // LIFFを使用可能にする初期処理
  await liff
    .init({
      //liffId: import.meta.env.VITE_LIFF_ID
      liffId: '2006899352-ndBbWrOK'
  
    })
    .catch(
      function(error) {
        alert("エラーにより画面が表示できませんでした。(" + error + ")");
        return;
      }
    );

  // LINEのユーザID
  let lineId;

  await liff
    .getProfile()
    .then(
        function(profile) {
          // LINE ID格納
          lineId = profile.userId;
        }
      )
    .catch(
      function(error) {
        alert("getProfile Error"+error);
        return;
      }
    );
  return lineId;
}