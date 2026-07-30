const faqs = [
  {
    question: "Is InterviewAce AI free to use?",
    answer:
      "Yes. You can start practicing interviews for free with basic AI analysis.",
  },
  {
    question: "Does it analyze facial expressions?",
    answer:
      "Yes. Our AI detects emotions, eye contact, head pose, and confidence.",
  },
  {
    question: "Can I download my interview report?",
    answer:
      "Yes. After each interview you can download a detailed PDF report.",
  },
  {
    question: "Which companies is it useful for?",
    answer:
      "It helps prepare for interviews at Google, Amazon, Microsoft, Meta, TCS, Infosys, Wipro and many more.",
  },
];

const FAQ = () => {
  return (
    <section className="bg-slate-900 py-28">
      <div className="mx-auto max-w-5xl px-6">

        <h2 className="text-center text-5xl font-bold text-white">
          Frequently Asked Questions
        </h2>

        <p className="mt-4 text-center text-slate-400">
          Everything you need to know about InterviewAce AI.
        </p>

        <div className="mt-16 space-y-6">

          {faqs.map((faq, index) => (
            <div
              key={index}
              className="rounded-2xl border border-slate-700 bg-slate-950 p-6"
            >
              <h3 className="text-xl font-semibold text-white">
                {faq.question}
              </h3>

              <p className="mt-4 text-slate-400 leading-8">
                {faq.answer}
              </p>
            </div>
          ))}

        </div>

      </div>
    </section>
  );
};

export default FAQ;