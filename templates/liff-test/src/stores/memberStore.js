import {defineStore} from 'pinia';

export const useMemberStore = defineStore(
  'member',
  {
    state: () => ({
      name: "",
      email: "",
      points: 0,
      note: "", 
    }),
    getters: {
      getMember: (state) => {
        return state.member;
      }
    },
    actions: {
      update(
        name,
        email,
        points,
        note
      ) {
        this.name = name;
        this.email = email;
        this.points = points;
        this.note = note;
      }
    },
  }
)