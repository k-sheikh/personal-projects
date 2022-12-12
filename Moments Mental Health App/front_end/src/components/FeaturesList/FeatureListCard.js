import './FeaturesListCard.css'
const FeatureListCard = ({image, title, subtitle, alt}) => {
    return (
        <div className="FeatureListCard">
            <img 
            className="FeatureListImage"
            src={image} 
            alt={alt}>
            </img>
            <h2>{title}</h2>
            <h3>{subtitle}</h3>
        </div>
    )
}

export default FeatureListCard
