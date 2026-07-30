import {
  Brain,
  Camera,
  Mic,
  Eye,
  BarChart3,
  FileText,
} from "lucide-react";

const features = [
  {
    icon: <Brain size={34} />,
    title: "AI Emotion Analysis",
    description:
      "Detect confidence, nervousness, happiness, stress and facial emotions using AI.",
  },
  {
    icon: <Camera size={34} />,
    title: "Face & Head Tracking",
    description:
      "Analyze face position, posture, smile detection and interview presence.",
  },
  {
    icon: <Eye size={34} />,
    title: "Eye Contact Detection",
    description:
      "Measure eye contact percentage and attention throughout the interview.",
  },
  {
    icon: <Mic size={34} />,
    title: "Speech Analysis",
    description:
      "Evaluate speech speed, pauses, fillers and pronunciation quality.",
  },
  {
    icon: <BarChart3 size={34} />,
    title: "Performance Dashboard",
    description:
      "Interactive graphs showing confidence, emotion and communication metrics.",
  },
  {
    icon: <FileText size={34} />,
    title: "AI Interview Report",
    description:
      "Generate a professional PDF report with strengths, weaknesses and suggestions.",
  },
];

const Features = () => {
  return (
    <section className="bg-slate-950 py-32">
      <div className="mx-auto max-w-7xl px-6">

        <h2 className="text-center text-5xl font-bold text-white">
          Powerful AI Features
        </h2>

        <p className="mx-auto mt-6 max-w-3xl text-center text-lg text-slate-400">
          InterviewAce AI evaluates your complete interview performance
          using Computer Vision, Speech Analysis and Artificial Intelligence.
        </p>

        <div className="mt-20 grid gap-8 md:grid-cols-2 lg:grid-cols-3">

          {features.map((feature, index) => (
            <div
              key={index}
              className="rounded-2xl border border-slate-800 bg-slate-900 p-8 transition hover:-translate-y-2 hover:border-blue-500"
            >
              <div className="mb-6 text-blue-500">
                {feature.icon}
              </div>

              <h3 className="mb-4 text-2xl font-semibold text-white">
                {feature.title}
              </h3>

              <p className="text-slate-400">
                {feature.description}
              </p>
            </div>
          ))}

        </div>

      </div>
    </section>
  );
};

export default Features;