import {defineStore} from 'pinia';

export const useLineStore = defineStore(
  'line',
  {
    state: () => ({
      id: "",
    }),
    getters: {
      getId: (state) => {
        return state.id;
      }
    },
    actions: {
      setId(id) {
        this.id = id;
      }
    },
  }
)