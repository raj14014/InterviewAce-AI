import { motion } from "framer-motion";
import { FaRobot } from "react-icons/fa";

const Navbar = () => {
  return (
    <motion.nav
      initial={{ y: -80, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6 }}
      className="fixed top-0 left-0 w-full z-50 backdrop-blur-md bg-slate-950/70 border-b border-slate-800"
    >
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">

        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="bg-blue-600 p-2 rounded-xl">
            <FaRobot className="text-white text-xl" />
          </div>

          <div>
            <h1 className="font-bold text-2xl text-white">
              InterviewAce AI
            </h1>
          </div>
        </div>

        {/* Menu */}
        <ul className="hidden md:flex gap-10 text-slate-300">

          <li className="hover:text-white cursor-pointer transition">
            Features
          </li>

          <li className="hover:text-white cursor-pointer transition">
            About
          </li>

          <li className="hover:text-white cursor-pointer transition">
            Pricing
          </li>

        </ul>

        {/* Buttons */}
        <div className="flex gap-4">

          <button className="text-white hover:text-blue-400 transition">
            Login
          </button>

          <button className="bg-blue-600 hover:bg-blue-700 px-5 py-2 rounded-xl transition">
            Get Started
          </button>

        </div>

      </div>
    </motion.nav>
  );
};

export default Navbar;