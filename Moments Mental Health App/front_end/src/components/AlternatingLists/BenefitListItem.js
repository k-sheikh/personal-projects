import "./BenefitListItem.css";

const BenefitListItem = ({
  image,
  subtitle,
  alt,
  textClass,
  reverse = false,
}) => {
  return (
    <div className="BenefitListCard">
      <img
        src={image}
        alt={alt}
        className={`BenefitListImage ${reverse ? "second" : "first"}`}
      ></img>
      <div className={`${textClass} ${reverse ? "first" : "second"}`}>
        <h3>{subtitle}</h3>
      </div>
    </div>
  );
};

export default BenefitListItem;
