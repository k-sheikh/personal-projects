import React from "react";
import MomentsCard from "./MomentsCard";
import "./MomentsList.css";
import { BiLeftArrow, BiRightArrow } from "react-icons/bi";
import { DECREMENT_SELECTION, INCREMENT_SELECTION } from "./MomentsTypes";

const MomentsModal = (props) => {
  const { dispatch } = props;

  const onNext = () => dispatch({ type: INCREMENT_SELECTION });
  const onPrevious = () => dispatch({ type: DECREMENT_SELECTION });

  const arrowSize = "2rem";
  return (
    <div className="selection-container">
      <div className="select-previous" onClick={() => onNext()}>
        <BiLeftArrow size={arrowSize} />
      </div>
      <div className="selection-card">
        <MomentsCard {...props} />
      </div>
      <div className="select-next" onClick={() => onPrevious()}>
        <BiRightArrow size={arrowSize} />
      </div>
    </div>
  );
};

export default MomentsModal;
