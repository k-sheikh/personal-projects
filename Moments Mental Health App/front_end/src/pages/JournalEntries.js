import React, {useEffect } from 'react'
import Footer from '../components/Footer/Footer'
import AuthNavbar from '../components/Header/AuthNavbar'
import JournalEntryList from '../components/JournalEntries/JournalEntryList'

const JournalEntries = ({onDelete, invalidateToken, setJournalEntries, journalEntries}) => {
    // fetch all entries

    useEffect(() => {
        const token = localStorage.getItem("moments_token")
        const fetchEntries = async () => {
        const res = await fetch('/entry/', {
            method: 'GET',
            headers: {
            'Content-type': 'application/json',
            'Authorization': `token ${token}`
            },
        })
        const data = await res.json()
        setJournalEntries([...data])
        return data
        }
        fetchEntries()
    },[setJournalEntries])
    return (
        <div>
            <AuthNavbar
            invalidateToken= { invalidateToken }
            />

            <JournalEntryList
            onDelete={onDelete}
            journalEntries={journalEntries}
            />
            
            <Footer/>
            
        </div>
    )
}

export default JournalEntries
