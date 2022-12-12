import "./BenefitListItem.css";
// import {Link} from 'react-router-dom'

const JournallingListItem = ({
  image,
  subtitle,
  alt,
  textClass,
  reverse = false,
  event,
  linkTo
}) => {

  
  return (
    <div className="BenefitListCard">
      <img
        src={image}
        alt={alt}
        className={`BenefitListImage ${reverse ? "second" : "first"}`}
      ></img>
      <div className={`${textClass} ${reverse ? "first" : "second"}`}>

       {/* <div className="formButton">
          {linkTo ? 
                <Link to={linkTo}>
                <Button 
                buttonStyle="btn--blue" 
                text= {subtitle} 
                />
                </Link>
                 : 
                <Button 
                buttonStyle="btn--blue" 
                text= {subtitle} 
                event={event}
                />
                }
                
        </div> */}
        
      </div>
    </div>
  );
};

export default JournallingListItem;
