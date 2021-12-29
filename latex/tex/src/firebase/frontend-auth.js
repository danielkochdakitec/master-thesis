const useAuthState = () => {
  const auth = useContext(AuthContext)

  return { ...auth, isAuthenticated: auth.user != null }
}

function PrivateRoute({ children }) {
  const { isAuthenticated } = useAuthState()

  return isAuthenticated ? children : <Navigate to="/login" />;
}

function PublicRoute({ children }) {
  const { isAuthenticated } = useAuthState()

  return isAuthenticated ? <Navigate to="/" /> : children;
}