import { Settings } from "@mui/icons-material";
import {
  AppBar,
  Avatar,
  createTheme,
  CssBaseline,
  Grid,
  IconButton,
  ThemeProvider,
  Toolbar,
  Typography,
} from "@mui/material";
import { MD5 } from "crypto-js";
import React from "react";
import { Navigate, Outlet } from "react-router-dom";
import TabMenu from "../components/TabMenu";

const theme = createTheme({
  palette: {
    background: { default: "#f3fafc" },
  },
});

function Layout() {
  const user = JSON.parse(
    localStorage.getItem("User") || sessionStorage.getItem("User") || "null"
  );

  if (!user) {
    return <Navigate to="/auth" />;
  }

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Grid container sx={{ height: "100vh" }}>
        <Grid
          item
          xs={4}
          sx={{
            display: "flex",
            flexDirection: "column",
            backgroundColor: "white",
            borderRight: 1,
            borderColor: "lightgray",
          }}
        >
          <AppBar position="relative">
            <Toolbar>
              <Avatar
                sx={{ mr: 2 }}
                alt={user.name}
                src={
                  "https://www.gravatar.com/avatar/" +
                  MD5(user.email.toLowerCase())
                }
              />
              <Typography
                variant="h6"
                color="inherit"
                noWrap
                sx={{ flexGrow: 1 }}
              >
                {user.name}
              </Typography>
              <IconButton aria-label="settings" color="default">
                <Settings />
              </IconButton>
            </Toolbar>
          </AppBar>
          <TabMenu />
        </Grid>
        <Grid item xs={8}>
          <Outlet />
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

export default Layout;
