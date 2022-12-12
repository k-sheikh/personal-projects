import JournallingListItem from "./JournallingListItem";
import guided from "../../static/guided.svg";
import freestyle from "../../static/freestyle.svg";
import browse from "../../static/browse.svg";
import browse_journal from "../../static/browse_journal.svg";
import moments from "../../static/moments.svg";
// import "./BenefitListItem.css";
import "./AuthListItem.css"
import Button from "../Button/Button";
import { Link } from "react-router-dom"

const AlternatingListAuthHomePage = ({journallingModal, guidedJournallingModal, momentsModal}) => {
  return (

    <div className="AuthPage">
      <div className="AuthListGrid">

        <div className="AuthListBox">
          <div className="AuthListImage">
            <JournallingListItem
            image={freestyle}
            alt="Woman facing a big journal and writing"
            />
          </div>
          <div className="AuthListText">
            <Button
            buttonStyle="btn--darkblue"
            text="Freestyle Journalling"
            event={journallingModal}
            />
          {/* <JournallingListItem
            subtitle="Freestyle Journalling"
            textClass="TextContainerRight"
            event={journallingModal}
            /> */}
          </div>
        </div>

        <div className="AuthListBox">
          <div className="AuthListText">
            <Button
            buttonStyle="btn--darkblue"
            text="Guided Journalling"
            event={guidedJournallingModal}
            />
            {/* <JournallingListItem
              subtitle="Guided Journalling"
              textClass="TextContainerLeft"
              event={guidedJournallingModal}
              /> */}
          </div>
          <div className="AuthListImage">
            <JournallingListItem
              image={guided}
              alt="Car on a road"
              />
          </div>
        </div>

        <div className="AuthListBox">
          <div className="AuthListImage">
          <JournallingListItem
              image={moments}
              alt="Car on a road"
              />
          </div>
          <div className="AuthListText">
            <Button
            buttonStyle="btn--darkblue"
            text="Add moments"
            event={momentsModal}
            />
            {/* <JournallingListItem
              subtitle="Add Moments"
              textClass="TextContainerRight"
              event={momentsModal}                
              /> */}
          </div>
        </div>

        <div className="AuthListBox">
          <div className="AuthListText">
            <Link to="./browse-moments">
            <Button
            buttonStyle="btn--darkblue"
            text="Browse moments"
            linkTo='/browse-moments'
            />
            </Link>
            {/* <JournallingListItem
              subtitle="Browse moments"
              textClass="TextContainerLeft"
              linkTo='/browse-moments'
              /> */}
          </div>
          <div className="AuthListImage">
            <JournallingListItem
              image={browse}
              alt="Man standing in front of a photo album"
              />
          </div>
        </div>

        <div className="AuthListBox">
          <div className="AuthListImage">
            <JournallingListItem
              image={browse_journal}
              alt="Man facing a page with content"
              />
          </div>
          <div className="AuthListText">
            <Link to="./browse-journal">
              <Button
              buttonStyle="btn--darkblue"
              text="Browse journal entries"
              linkTo='/browse-journal'
              />
            </Link>
            {/* <JournallingListItem
              subtitle="Browse Journal Entries"
              textClass="TextContainerRight"
              linkTo='/browse-journal'
              /> */}
          </div>
        </div>

      </div>
    </div>

// 
// 
// 

  // <div className="BenefitListVerticalContainer">
  //           <div className="BenefitListContainer">
  //               <JournallingListItem
  //               image={freestyle}
  //               subtitle="Freestyle Journalling"
  //               alt="Woman facing a big journal and writing"
  //               textClass="TextContainerRight"
  //               event={journallingModal}
  //               />

                // <JournallingListItem
                // image={guided}
                // subtitle="Guided Journalling"
                // alt="Car on a road"
                // textClass="TextContainerLeft"
                // reverse={true}
                // event={guidedJournallingModal}                
                // />

                // <JournallingListItem
                // image={moments}
                // subtitle="Add Moments"
                // alt="Car on a road"
                // textClass="TextContainerRight"
                // event={momentsModal}                
                // />

                // <JournallingListItem
                // image={browse}
                // subtitle="Browse moments"
                // alt="Man standing in front of a photo album"
                // textClass="TextContainerLeft"
                // reverse={true}
                // linkTo='/browse-moments'
                // />

        //         <JournallingListItem
        //         image={browse_journal}
        //         subtitle="Browse Journal Entries"
        //         alt="Man facing a page with content"
        //         textClass="TextContainerRight"
        //         linkTo='/browse-journal'
        //         />

        //     </div>

        // </div>
    )
}

export default AlternatingListAuthHomePage
