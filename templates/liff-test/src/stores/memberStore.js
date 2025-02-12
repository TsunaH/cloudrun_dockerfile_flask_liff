import {defineStore} from 'pinia';

export const useMemberStore = defineStore(
    'member',
    {
    state: () => {
      return {
        name: "",
        email: "",
        points: 0,
        note: "", 
      };
    },
    getters: {
      getMember: (state) => {
        return state.member;
      }
    },
    actions: {
      update(state, member) {
        state.member = member;

      }
    }
  }
)