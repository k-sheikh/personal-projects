import {
  GET_MOMENTS,
  SELECT_MOMENT,
  CLEAR_SELECTION,
  INCREMENT_SELECTION,
  DECREMENT_SELECTION,
  DELETE_MOMENT,
} from "./MomentsTypes";

export const initialState = {
  moments: [],
  selection: null,
  pk_list: [],
};

export function momentsReducer(state, action) {
  const momentsLength = state.moments.length;
  let selectionIndex;
  switch (action.type) {
    case GET_MOMENTS:
      return {
        ...state,
        moments: action.payload,
        pk_list: action.payload?.map?.((moment) => moment.pk),
      };
    case SELECT_MOMENT:
      return { ...state, selection: action.payload };
    case CLEAR_SELECTION:
      return { ...state, selection: null };
    case INCREMENT_SELECTION:
      selectionIndex = state.pk_list.indexOf(state.selection?.pk);
      const nextIndex =
        momentsLength > selectionIndex + 1 ? selectionIndex + 1 : 0;
      return { ...state, selection: state.moments[nextIndex] };
    case DECREMENT_SELECTION:
      selectionIndex = state.pk_list.indexOf(state.selection?.pk);
      const previousIndex =
        0 < selectionIndex ? selectionIndex - 1 : momentsLength - 1;
      return { ...state, selection: state.moments[previousIndex] };
    case DELETE_MOMENT:
      return {
        ...state,
        moments: state.moments.filter((moment) => moment.pk !== action.payload),
        selection: null,
      };
    default:
      return state;
  }
}
