import AuthLayout from "../../components/auth/AuthLayout";
import LoginForm from "../../components/auth/LoginForm";

const LoginPage = () => {
  return (
    <AuthLayout
      title="Welcome Back"
      subtitle="Login to continue your AI interview journey."
    >
      <LoginForm />
    </AuthLayout>
  );
};

export default LoginPage;