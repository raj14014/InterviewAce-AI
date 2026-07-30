import Navbar from "../../components/layout/Navbar";
import Hero from "../../components/home/Hero";
import TrustedCompanies from "../../components/home/TrustedCompanies";
import Features from "../../components/home/Features";
import DashboardPreview from "../../components/home/DashboardPreview";
import Stats from "../../components/home/Stats";
import Testimonials from "../../components/home/Testimonials";
import FAQ from "../../components/home/FAQ";
import Pricing from "../../components/home/Pricing";
import Footer from "../../components/layout/Footer";

const LandingPage = () => {
  return (
    <>
      <Navbar />
      <Hero />
      <TrustedCompanies />
      <Features />
      <DashboardPreview />
      <Stats />
      <Testimonials />
      <FAQ />
      <Pricing />
      <Footer />
    </>
  );
};

export default LandingPage;