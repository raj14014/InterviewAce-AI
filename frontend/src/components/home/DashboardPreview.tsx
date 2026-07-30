import {
  Camera,
  Eye,
  Mic,
  Brain,
  Smile,
  BarChart3,
} from "lucide-react";

const metrics = [
  {
    icon: <Camera size={24} />,
    title: "Face Detection",
    value: "Detected",
    color: "text-green-400",
  },
  {
    icon: <Eye size={24} />,
    title: "Eye Contact",
    value: "88%",
    color: "text-blue-400",
  },
  {
    icon: <Mic size={24} />,
    title: "Voice Clarity",
    value: "91%",
    color: "text-cyan-400",
  },
  {
    icon: <Brain size={24} />,
    title: "Confidence",
    value: "89%",
    color: "text-purple-400",
  },
  {
    icon: <Smile size={24} />,
    title: "Emotion",
    value: "Happy",
    color: "text-yellow-400",
  },
  {
    icon: <BarChart3 size={24} />,
    title: "Interview Score",
    value: "92%",
    color: "text-green-400",
  },
];

const DashboardPreview = () => {
  return (
    <section className="bg-slate-900 py-32">
      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">
          <h2 className="text-5xl font-bold text-white">
            Live AI Dashboard
          </h2>

          <p className="mt-5 text-lg text-slate-400">
            Monitor interview performance in real time with AI-powered analytics.
          </p>
        </div>

        <div className="mt-20 rounded-3xl border border-slate-800 bg-slate-950 p-8 shadow-2xl">

          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">

            {metrics.map((metric, index) => (
              <div
                key={index}
                className="rounded-2xl border border-slate-800 bg-slate-900 p-6 transition hover:border-blue-500"
              >
                <div className={`${metric.color} mb-4`}>
                  {metric.icon}
                </div>

                <h3 className="text-xl font-semibold text-white">
                  {metric.title}
                </h3>

                <p className={`mt-3 text-3xl font-bold ${metric.color}`}>
                  {metric.value}
                </p>
              </div>
            ))}

          </div>

          <div className="mt-20 rounded-2xl border border-slate-800 bg-slate-900 p-8">

            <h3 className="mb-6 text-2xl font-semibold text-white">
              Performance Overview
            </h3>

            <div className="space-y-5">

              <div>
                <div className="mb-2 flex justify-between text-white">
                  <span>Confidence</span>
                  <span>89%</span>
                </div>

                <div className="h-3 rounded-full bg-slate-700">
                  <div className="h-3 w-[89%] rounded-full bg-blue-500"></div>
                </div>
              </div>

              <div>
                <div className="mb-2 flex justify-between text-white">
                  <span>Eye Contact</span>
                  <span>88%</span>
                </div>

                <div className="h-3 rounded-full bg-slate-700">
                  <div className="h-3 w-[88%] rounded-full bg-green-500"></div>
                </div>
              </div>

              <div>
                <div className="mb-2 flex justify-between text-white">
                  <span>Voice Clarity</span>
                  <span>91%</span>
                </div>

                <div className="h-3 rounded-full bg-slate-700">
                  <div className="h-3 w-[91%] rounded-full bg-cyan-500"></div>
                </div>
              </div>

            </div>

          </div>

        </div>

      </div>
    </section>
  );
};

export default DashboardPreview;