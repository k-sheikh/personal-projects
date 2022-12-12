import React from "react";
import { SELECT_MOMENT, DELETE_MOMENT } from "./MomentsTypes";
import Icon from "../Icon/Icon";
const MomentsCard = ({ moment, dispatch }) => {
  if (!moment) {
    return null;
  }
  const deleteCard = async () => {
    const pk = moment.pk;
    dispatch({ type: DELETE_MOMENT, payload: pk });

    const token = localStorage.getItem("moments_token");
    await fetch(`/moment/${pk}`, {
      method: "delete",
      headers: {
        Authorization: `token ${token}`,
      },
    });
  };

  const onDeleteClick = (e) => {
    e.stopPropagation();
    deleteCard();
  };

  return (
    <>
    {moment.noMoments ?
    <div className="moment-no-moment-container">
      <div className="moment-card-no-moment">
        <div className="moment-text">
          <h3>{moment.description}</h3>
        </div> 
      </div>
    </div>
    : 
    <div
      className="moment-card"
      onClick={() => dispatch({ type: SELECT_MOMENT, payload: moment })}
    >
      
      <div className="moment-text">
        <h3>{moment.date}</h3>
        <br />
        <h3>{moment.description}</h3>
      </div>

      <img src={moment.image} alt="" className="moment-image" />
      <Icon className="deckIcon" event={(e) => onDeleteClick(e)} />
    </div>
    }
    </>
    
  );
};

export default MomentsCard;
