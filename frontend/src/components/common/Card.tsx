import React from "react";

interface CardProps {
  children: React.ReactNode;
  className?: string;
}

const Card = ({ children, className = "" }: CardProps) => {
  return (
    <div
      className={`
        bg-slate-900/70
        backdrop-blur-lg
        border
        border-slate-700
        rounded-2xl
        shadow-xl
        p-6
        transition-all
        duration-300
        hover:border-blue-500
        hover:shadow-blue-500/20
        ${className}
      `}
    >
      {children}
    </div>
  );
};

export default Card;