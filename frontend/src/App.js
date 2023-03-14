import Header from "./Header";
import { ThemeProvider } from '@mui/material/styles';
import { theme } from './theme'
import MainWrapper from "./MainWrapper";

function App() {
  return (
    <div >
      <ThemeProvider theme={theme}>
        <Header />
        <MainWrapper>
        </MainWrapper>
      </ThemeProvider>
    </div>
  );
}

export default App;
