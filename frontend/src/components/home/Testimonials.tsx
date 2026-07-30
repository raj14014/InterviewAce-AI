const testimonials = [
  {
    name: "Rahul Sharma",
    role: "Software Engineer",
    company: "Google",
    review:
      "InterviewAce AI helped me improve my confidence and communication. I cracked my dream job.",
  },
  {
    name: "Priya Singh",
    role: "ML Engineer",
    company: "Microsoft",
    review:
      "The AI feedback on eye contact and speech analysis was incredibly accurate.",
  },
  {
    name: "Aman Verma",
    role: "Backend Developer",
    company: "Amazon",
    review:
      "Best interview preparation platform I have ever used.",
  },
];

const Testimonials = () => {
  return (
    <section className="bg-slate-950 py-28">
      <div className="mx-auto max-w-7xl px-6">
        <h2 className="text-center text-5xl font-bold text-white">
          What Our Users Say
        </h2>

        <p className="mt-4 text-center text-slate-400">
          Thousands of students trust InterviewAce AI.
        </p>

        <div className="mt-16 grid gap-8 lg:grid-cols-3">
          {testimonials.map((item, index) => (
            <div
              key={index}
              className="rounded-2xl border border-slate-800 bg-slate-900 p-8"
            >
              <p className="text-slate-300 leading-8">
                "{item.review}"
              </p>

              <div className="mt-8">
                <h3 className="text-xl font-semibold text-white">
                  {item.name}
                </h3>

                <p className="text-slate-400">
                  {item.role} • {item.company}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Testimonials;