import {
  ArrowBack,
  ArrowDownward,
  ArrowForward,
  Refresh,
  ThumbDown,
  ThumbUp,
} from "@mui/icons-material";
import { Card, CardMedia, Chip, Fab } from "@mui/material";
import Box from "@mui/material/Box";
import React from "react";

export default function HomePage() {
  return (
    <Box
      component="main"
      sx={{
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Card
        sx={{
          width: 450,
          maxHeight: "fit-content",
          marginTop: "4rem",
          marginBottom: "0.5rem",
        }}
      >
        <CardMedia
          component="img"
          image="/static/img/Abstract_Brushstroke_Print_Pencil_Skirt/img_00000001.jpg"
        />
      </Card>
      <Box
        sx={{
          display: "flex",
          marginBottom: "4rem",
          gap: "1rem",
        }}
      >
        <Fab aria-label="dislike" color="error">
          <ThumbDown />
        </Fab>
        <Fab aria-label="indiferent">
          <Refresh />
        </Fab>
        <Fab aria-label="like" color="success">
          <ThumbUp />
        </Fab>
      </Box>
      <Box sx={{ display: "flex", gap: "1rem" }}>
        <Chip icon={<ArrowBack />} label="Dislike" />
        <Chip icon={<ArrowDownward />} label="Indiferent" />
        <Chip icon={<ArrowForward />} label="Like" />
      </Box>
    </Box>
  );
}
