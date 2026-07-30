import { useState } from "react";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { User, Mail, Lock, Eye, EyeOff } from "lucide-react";

type RegisterData = {
  name: string;
  email: string;
  password: string;
  confirmPassword: string;
};

const RegisterForm = () => {
  const [showPassword, setShowPassword] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<RegisterData>();

  const onSubmit = (data: RegisterData) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">

      {/* Full Name */}
      <div>
        <label className="mb-2 block text-white">
          Full Name
        </label>

        <div className="flex items-center rounded-xl border border-slate-700 bg-slate-800 px-4">
          <User className="text-slate-400" size={20} />

          <input
            type="text"
            placeholder="Enter your full name"
            className="w-full bg-transparent p-4 text-white outline-none"
            {...register("name", {
              required: "Full name is required",
            })}
          />
        </div>

        {errors.name && (
          <p className="mt-2 text-sm text-red-500">
            {errors.name.message}
          </p>
        )}
      </div>

      {/* Email */}
      <div>
        <label className="mb-2 block text-white">
          Email
        </label>

        <div className="flex items-center rounded-xl border border-slate-700 bg-slate-800 px-4">
          <Mail className="text-slate-400" size={20} />

          <input
            type="email"
            placeholder="Enter your email"
            className="w-full bg-transparent p-4 text-white outline-none"
            {...register("email", {
              required: "Email is required",
            })}
          />
        </div>

        {errors.email && (
          <p className="mt-2 text-sm text-red-500">
            {errors.email.message}
          </p>
        )}
      </div>

      {/* Password */}
      <div>
        <label className="mb-2 block text-white">
          Password
        </label>

        <div className="flex items-center rounded-xl border border-slate-700 bg-slate-800 px-4">
          <Lock className="text-slate-400" size={20} />

          <input
            type={showPassword ? "text" : "password"}
            placeholder="Enter your password"
            className="w-full bg-transparent p-4 text-white outline-none"
            {...register("password", {
              required: "Password is required",
            })}
          />

          <button
            type="button"
            onClick={() => setShowPassword(!showPassword)}
          >
            {showPassword ? (
              <EyeOff className="text-slate-400" size={20} />
            ) : (
              <Eye className="text-slate-400" size={20} />
            )}
          </button>
        </div>

        {errors.password && (
          <p className="mt-2 text-sm text-red-500">
            {errors.password.message}
          </p>
        )}
      </div>

      {/* Confirm Password */}
      <div>
        <label className="mb-2 block text-white">
          Confirm Password
        </label>

        <div className="flex items-center rounded-xl border border-slate-700 bg-slate-800 px-4">
          <Lock className="text-slate-400" size={20} />

          <input
            type="password"
            placeholder="Confirm your password"
            className="w-full bg-transparent p-4 text-white outline-none"
            {...register("confirmPassword", {
              required: "Confirm password is required",
            })}
          />
        </div>

        {errors.confirmPassword && (
          <p className="mt-2 text-sm text-red-500">
            {errors.confirmPassword.message}
          </p>
        )}
      </div>

      {/* Submit Button */}
      <button
        type="submit"
        className="w-full rounded-xl bg-blue-600 py-4 font-semibold text-white transition hover:bg-blue-700"
      >
        Create Account
      </button>

      {/* Login Link */}
      <p className="text-center text-slate-400">
        Already have an account?{" "}
        <Link
          to="/login"
          className="font-semibold text-blue-500 hover:text-blue-400"
        >
          Login
        </Link>
      </p>

    </form>
  );
};

export default RegisterForm;