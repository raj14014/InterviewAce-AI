const stats = [
  {
    number: "50K+",
    title: "Mock Interviews",
  },
  {
    number: "25K+",
    title: "Students",
  },
  {
    number: "95%",
    title: "Success Rate",
  },
  {
    number: "150+",
    title: "Companies",
  },
];

const Stats = () => {
  return (
    <section className="bg-slate-950 py-28">
      <div className="mx-auto max-w-7xl px-6">
        <div className="grid grid-cols-2 gap-8 lg:grid-cols-4">
          {stats.map((item, index) => (
            <div
              key={index}
              className="rounded-2xl border border-slate-800 bg-slate-900 p-10 text-center"
            >
              <h2 className="text-5xl font-bold text-blue-500">
                {item.number}
              </h2>

              <p className="mt-4 text-lg text-slate-400">
                {item.title}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Stats;