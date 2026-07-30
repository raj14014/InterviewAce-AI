import { Link } from "react-router-dom";
import Button from "../common/Button";
import Logo from "../common/Logo";

const Navbar = () => {
  return (
    <nav className="fixed top-0 left-0 w-full z-50 bg-slate-950/80 backdrop-blur-md border-b border-slate-800">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-6 py-4">

        <Logo />

        <div className="hidden md:flex items-center gap-8 text-slate-300">

          <Link to="/">Home</Link>

          <Link to="/features">Features</Link>

          <Link to="/pricing">Pricing</Link>

          <Link to="/about">About</Link>

        </div>

        <div className="flex items-center gap-4">

          <Link to="/login">
            <Button variant="outline">
              Login
            </Button>
          </Link>

          <Link to="/register">
            <Button>
              Get Started
            </Button>
          </Link>

        </div>

      </div>
    </nav>
  );
};

export default Navbar;