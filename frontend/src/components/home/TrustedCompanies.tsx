const TrustedCompanies = () => {
  return (
    <section className="bg-slate-900 py-16">
      <div className="mx-auto max-w-7xl px-6">

        <h2 className="mb-10 text-center text-3xl font-bold text-white">
          Trusted by Developers Worldwide
        </h2>

        <div className="grid grid-cols-2 gap-6 text-center md:grid-cols-4">

          <div className="rounded-xl bg-slate-800 p-6 text-white">
            OpenAI
          </div>

          <div className="rounded-xl bg-slate-800 p-6 text-white">
            Google
          </div>

          <div className="rounded-xl bg-slate-800 p-6 text-white">
            Microsoft
          </div>

          <div className="rounded-xl bg-slate-800 p-6 text-white">
            NVIDIA
          </div>

          <div className="rounded-xl bg-slate-800 p-6 text-white">
            Amazon
          </div>

          <div className="rounded-xl bg-slate-800 p-6 text-white">
            Meta
          </div>

          <div className="rounded-xl bg-slate-800 p-6 text-white">
            GitHub
          </div>

          <div className="rounded-xl bg-slate-800 p-6 text-white">
            Intel
          </div>

        </div>

      </div>
    </section>
  );
};

export default TrustedCompanies;