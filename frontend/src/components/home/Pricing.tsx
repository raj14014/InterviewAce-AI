const plans = [
  {
    title: "Free",
    price: "₹0",
    features: [
      "1 Mock Interview / Day",
      "Basic AI Feedback",
      "Emotion Detection",
      "PDF Report",
    ],
  },
  {
    title: "Pro",
    price: "₹499/mo",
    features: [
      "Unlimited Interviews",
      "Advanced AI Analysis",
      "Voice Analytics",
      "Company-wise Questions",
      "Priority Support",
    ],
  },
  {
    title: "Enterprise",
    price: "Custom",
    features: [
      "College Dashboard",
      "Student Analytics",
      "Placement Reports",
      "Unlimited Users",
      "Dedicated Support",
    ],
  },
];

const Pricing = () => {
  return (
    <section className="bg-slate-950 py-28">
      <div className="mx-auto max-w-7xl px-6">

        <h2 className="text-center text-5xl font-bold text-white">
          Pricing Plans
        </h2>

        <p className="mt-4 text-center text-slate-400">
          Choose the perfect plan for your interview preparation.
        </p>

        <div className="mt-16 grid gap-8 lg:grid-cols-3">

          {plans.map((plan, index) => (
            <div
              key={index}
              className="rounded-3xl border border-slate-800 bg-slate-900 p-10"
            >
              <h3 className="text-3xl font-bold text-white">
                {plan.title}
              </h3>

              <p className="mt-4 text-5xl font-bold text-blue-500">
                {plan.price}
              </p>

              <div className="mt-8 space-y-4">
                {plan.features.map((feature, i) => (
                  <p key={i} className="text-slate-300">
                    ✓ {feature}
                  </p>
                ))}
              </div>

              <button className="mt-10 w-full rounded-xl bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700">
                Get Started
              </button>
            </div>
          ))}

        </div>

      </div>
    </section>
  );
};

export default Pricing;