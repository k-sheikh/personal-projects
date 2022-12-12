import React from "react";
import BenefitListItem from "./BenefitListItem";
import knowledge from "../../static/knowledge.svg";
import sleep from "../../static/sleep.svg";
import journal from "../../static/journal.svg";
import "./BenefitListItem.css";

const AlternatingListHomePage = () => {
  return (
    <div className="Section2">
      <div className="BenefitListGrid">
        
        <div className="BenefitListBox">
          <div className="BenefitListImage">
            <BenefitListItem
              image={sleep}
              alt="Woman Sleeping"
            />
          </div>
          <div className="BenefitListText">
            <h1>Journalling helps you sleep better</h1>
            <p>Research shows that journaling reduced bedtime worry and stress, increased sleep time, and improved sleep quality.</p>
          </div>
        </div>

        <div className="BenefitListBox">
          <div className="BenefitListText">
            <h1>Reduce stress and anxiety</h1>
            <p>Journaling is a highly recommended stress-management tool which can help reduce anxiety, lessen feelings of distress, and increase well-being</p>
          </div>
          <div className="BenefitListImage">
            <BenefitListItem
              image={journal}
              alt="Woman facing a big journal"
            />
          </div>
        </div>

        <div className="BenefitListBox">
          <div className="BenefitListImage">
            <BenefitListItem
              image={knowledge}
              alt="Woman gazing at a static page"
            />
          </div>
          <div className="BenefitListText">
              <h1>Learn from your own experiences</h1>
              <p> If you feel overwhelmed, journaling will help you reach clarity. By keeping a journal, you are adding a ritual to your life. You're giving yourself permission to spend time alone with your thoughts.</p>
          </div>
        </div>

      </div>
    </div>
  );
};


// const AlternatingListHomePage = () => {
//   return (
//     <div className="BenefitListVerticalContainer">
//       <div className="BenefitListContainer">
//         <BenefitListItem
//           image={sleep}
//           subtitle="Journaling helps you sleep better."
//           alt="Woman Sleeping"
//           textClass="TextContainerRight"
//         />

//         <BenefitListItem
//           image={journal}
//           subtitle="Journaling reduces stress and anxiety."
//           alt="Woman facing a big journal"
//           textClass="TextContainerLeft"
//           reverse={true}
//         />

//         <BenefitListItem
//           image={knowledge}
//           subtitle="Journaling helps you learn from your experiences."
//           alt="Woman gazing at a static page"
//           textClass="TextContainerRight"
//         />
//       </div>
//     </div>
//   );
// };

export default AlternatingListHomePage;
