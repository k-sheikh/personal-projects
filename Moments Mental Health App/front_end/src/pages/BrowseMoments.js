import MomentsList from "../components/BrowseMoments.js/MomentsList";
import Footer from '../components/Footer/Footer'
import AuthNavbar from '../components/Header/AuthNavbar'
const BrowseMoments = ({invalidateToken}) => {

  return (
      <>
      <AuthNavbar
      invalidateToken= { invalidateToken }
      />
      <MomentsList />
      <Footer />
      </>
  );
};

export default BrowseMoments;