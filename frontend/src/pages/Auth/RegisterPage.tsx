import AuthLayout from "../../components/auth/AuthLayout";
import RegisterForm from "../../components/auth/RegisterForm";

const RegisterPage = () => {
  return (
    <AuthLayout
      title="Create Account"
      subtitle="Start your AI interview journey today."
    >
      <RegisterForm />
    </AuthLayout>
  );
};

export default RegisterPage;