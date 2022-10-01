import {
  Container,
  createTheme,
  CssBaseline,
  ThemeProvider,
} from "@mui/material";
import React from "react";
import { Outlet } from "react-router-dom";

const theme = createTheme();

function PlainLayout() {
  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="sm">
        <CssBaseline />
        <Outlet />
      </Container>
    </ThemeProvider>
  );
}

export default PlainLayout;
