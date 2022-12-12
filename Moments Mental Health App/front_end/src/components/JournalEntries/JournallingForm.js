import Button from '../Button/Button'
import { useHistory } from "react-router-dom"
import './Journalling.css'
import { useState } from 'react';

function JournallingForm({id, prompt}) {
    let history= useHistory();
    const onSubmit = async (e) => {
        e.preventDefault();
        const entryForm = document.getElementById(id)
        const token = localStorage.getItem("moments_token")
        const body = new FormData(entryForm)

        if (!!prompt?.url){
          body.append("prompt", prompt.url)

        }

        const res = await fetch("/entry/", {
          method: "POST",
          body,
          headers: {
            Authorization: `token ${token}`,
          },
        });
        await res.json();
        entryForm.reset()
        history.push("/browse-journal");
      }
      const [preview, setPreview] = useState();

    return (
        
        <form id={id} onSubmit={onSubmit} >
            <input className="entry-title" type="text" name="title" id="title" placeholder="Entry title"/>
            <textarea className="entry-body" type="text" name="body" id="body" placeholder="Write your journal entry here..."/>
            <input className="entry-attach" type="file" name="image" id="image" onChange={(e) => {
            setPreview(URL.createObjectURL(e.target.files[0]));
          }} />
            <img src={preview} className="preview" alt="" />
            <div className="formButton">
                <Button 
                buttonStyle="btn--red" 
                type="submit"
                text= "Create Moment" 
                value="Create Moment"
                />
            </div>
        </form>
        
    )
}

export default JournallingForm
