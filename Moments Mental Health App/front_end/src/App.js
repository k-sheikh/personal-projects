import { Switch, BrowserRouter as Router, Route } from "react-router-dom";
import AuthHomePage from "./pages/AuthHomePage";
import { useState } from 'react';
import HomePage from "./pages/HomePage";
import BrowseMoments from "./pages/BrowseMoments";
import JournalEntries from "./pages/JournalEntries";


function App() {
  const [journalEntries, setJournalEntries] = useState([])
  const [token, setToken] = useState();
  const invalidateToken = () => {
    localStorage.removeItem('moments_token')
    setToken(false)
  }
  // const [newJournalEntry, setNewJournalEntry] = useState([])
  // setJournalEntries[...journalEntries, newEntry]

  // delete entry  
  const deleteEntry = async (id) => {
    const res = await fetch(`/entry/${id}/`, {
      method: 'DELETE',
      headers: { 
        'Content-Type': 'application/json',
        'Authorization': `token ${token}`
   }
    })
    if (res.status === 204) {
      // UI
      setJournalEntries(journalEntries.filter((e) => e.pk !== id))
    }
  }
  return (
    <Router>
      <Switch>
        <Route path="/browse-journal">
          <JournalEntries
          journalEntries={journalEntries}
          onDelete={deleteEntry}
          invalidateToken = {invalidateToken}
          setJournalEntries = {setJournalEntries}
          />
          
        </Route>

        <Route path="/browse-moments">
          <BrowseMoments 
          invalidateToken = {invalidateToken}
          />
        </Route>
        
        <Route path="/">
        {!token ? 
        <HomePage
        setToken = { setToken }
        /> : 
        <AuthHomePage
        token = {token}
        invalidateToken = { invalidateToken }
        />}
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
