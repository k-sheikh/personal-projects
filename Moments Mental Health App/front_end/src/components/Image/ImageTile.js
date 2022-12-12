import './ImageTile.css'

const ImageTile = ({image, title, alt}) => {
    return (
        <div className='center imageContainer'>
            <img 
            className='imageTile'
            src={image} 
            alt={alt}>
            </img>
            <h4 className="text">{title}</h4>
        </div>
    )
}

export default ImageTile
