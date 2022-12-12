import React from 'react'
import Icon from '../Icon/Icon'
import './Journalling.css'
const JournalEntryCard = ({id, onDelete, body, title, image, date, prompt}) => {
    return (
        <div className="card">
            {prompt ? <h3>{prompt}</h3> : <h3>{title}</h3>}
            
            <p>{body}</p>
            
            <img src={image} alt="" className="entry-image"/>
            <div className="journal-text">
            <strong>{date}</strong>
            </div>
            {!date ? null : <Icon 
            className="deckIcon"
            event={()=>onDelete(id)}
            />}
            
        </div>
    )
}

export default JournalEntryCard
