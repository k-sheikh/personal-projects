import FeatureListCard from './FeatureListCard'

import pen_icon from '../../static/pen_icon.svg'
import book_icon from '../../static/book_icon.svg'
import clock_icon from '../../static/clock_icon.svg'
import mobile_icon from '../../static/mobile_icon.svg'
import './FeaturesListCard.css'
const FeatureList = () => {
    return (
        <div className="FeatureListVerticalContainer">
            <div className="FeatureListContainer">
                <FeatureListCard
                image={pen_icon}
                title="Create Moments"
                subtitle="Add some snazzy moments from your life"
                alt="Pen"
                />

                <FeatureListCard
                image={book_icon}
                title="Relive your Moments"
                subtitle="Look back at some of your memories"
                alt="book"
                />

                <FeatureListCard
                image={clock_icon}
                title="Reflection"
                subtitle="Look back on past experiences"
                alt="clock"
                />

                <FeatureListCard
                image={mobile_icon}
                title="Portable"
                subtitle="View your journal on any device"
                alt="mobile"
                />
            </div>
        </div>
    )
}

export default FeatureList
