import { motion } from "framer-motion";
import { BrainCircuit, Camera, Mic, BarChart3 } from "lucide-react";

import Button from "../common/Button";
import Container from "../common/Container";

const Hero = () => {
  return (
    <section className="relative min-h-screen overflow-hidden bg-slate-950 pt-32">

      {/* Background Blur */}
      <div className="absolute left-10 top-20 h-72 w-72 rounded-full bg-blue-600/20 blur-3xl"></div>
      <div className="absolute right-10 bottom-20 h-72 w-72 rounded-full bg-cyan-500/20 blur-3xl"></div>

      <Container>
        <div className="grid min-h-[85vh] items-center gap-24 lg:grid-cols-2">

          {/* Left */}
          <motion.div
            initial={{ opacity: 0, x: -60 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
          >
            <span className="rounded-full border border-blue-500 px-4 py-2 text-sm text-blue-400">
              🚀 AI Powered Interview Preparation
            </span>

            <h1 className="mt-8 text-6xl font-extrabold leading-tight text-white lg:text-7xl">
              Ace Every{" "}
              <span className="text-blue-500">Interview</span>
              <br />
              With Artificial Intelligence
            </h1>

            <p className="mt-8 max-w-2xl text-xl leading-9 text-slate-400">
              Practice interviews with real-time AI analysis.
              Improve confidence, eye contact, facial expressions,
              communication skills, and receive detailed feedback instantly.
            </p>

            <div className="mt-10 flex flex-wrap gap-4">
              <Button size="lg">
                Start Free
              </Button>

              <Button variant="outline" size="lg">
                Watch Demo
              </Button>
            </div>

            <div className="mt-12 flex flex-wrap gap-10">

              <div>
                <h2 className="text-4xl font-bold text-white">95%</h2>
                <p className="text-slate-400">AI Accuracy</p>
              </div>

              <div>
                <h2 className="text-4xl font-bold text-white">25+</h2>
                <p className="text-slate-400">Interview Metrics</p>
              </div>

              <div>
                <h2 className="text-4xl font-bold text-white">Real-Time</h2>
                <p className="text-slate-400">AI Analysis</p>
              </div>

            </div>

          </motion.div>

          {/* Right */}
          <motion.div
            initial={{ opacity: 0, x: 60 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
          >

            <div className="w-full rounded-3xl border border-slate-800 bg-slate-900/80 p-10 shadow-2xl backdrop-blur-xl">

              <h2 className="mb-8 text-4xl font-bold text-white">
                Live AI Dashboard
              </h2>

              <div className="space-y-8">

                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <Camera className="text-blue-400" />
                    <span className="text-white">Face Detection</span>
                  </div>

                  <span className="text-green-400">Active</span>
                </div>

                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <Mic className="text-blue-400" />
                    <span className="text-white">Speech Analysis</span>
                  </div>

                  <span className="text-green-400">Active</span>
                </div>

                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <BrainCircuit className="text-blue-400" />
                    <span className="text-white">Emotion Detection</span>
                  </div>

                  <span className="text-green-400">Running</span>
                </div>

                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <BarChart3 className="text-blue-400" />
                    <span className="text-white">Confidence Score</span>
                  </div>

                  <span className="font-bold text-yellow-400">87%</span>
                </div>

              </div>

            </div>

          </motion.div>

        </div>
      </Container>

    </section>
  );
};

export default Hero;