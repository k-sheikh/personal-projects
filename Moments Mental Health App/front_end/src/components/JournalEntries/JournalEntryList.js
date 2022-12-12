import React from 'react'
import JournalEntryCard from './JournalEntryCard'
import './Journalling.css'
const JournalEntryList = ({journalEntries, onDelete}) => {
    return (
        <div className="gallery">
            <div className="gallery-container">
                {(journalEntries.length > 0) ?
                journalEntries.map(entry => (
                <div className="journal-entry">
                <JournalEntryCard
                key={entry.pk}
                id={entry.pk}
                onDelete={onDelete}
                date={entry.date}
                body={entry.body}
                title={entry.title}
                image={entry.image}
                prompt={entry.prompt}
                />
                </div>))
                : (
                <div className="no-entry-card-container">
                    <div className="no-entry-card">
                        <JournalEntryCard
                            title={"No entries to show"}
                        />
                    </div>
                </div>
                ) }
            </div>
        </div>
    )
}

export default JournalEntryList
