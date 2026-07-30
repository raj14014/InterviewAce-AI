import { useState } from "react";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { Eye, EyeOff, Mail, Lock } from "lucide-react";

type LoginData = {
  email: string;
  password: string;
};

const LoginForm = () => {
  const [showPassword, setShowPassword] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginData>();

  const onSubmit = (data: LoginData) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">

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

      {/* Login Button */}
      <button
        type="submit"
        className="w-full rounded-xl bg-blue-600 py-4 font-semibold text-white transition hover:bg-blue-700"
      >
        Login
      </button>

      {/* Register Link */}
      <p className="text-center text-slate-400">
        Don't have an account?{" "}
        <Link
          to="/register"
          className="font-semibold text-blue-500 hover:text-blue-400"
        >
          Register
        </Link>
      </p>

    </form>
  );
};

export default LoginForm;