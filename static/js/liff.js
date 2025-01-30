function main() {
  liff
    .init({
      liffId: "2006831755-QEdgjOA8"
    })
    .then(() => {
      liff.sendMessages([
        {
          type: "text",
          text: "Hello,World",
        },
      ]);
    });
}