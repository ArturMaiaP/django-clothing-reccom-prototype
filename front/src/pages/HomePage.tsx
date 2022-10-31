import {
  ArrowBack,
  ArrowDownward,
  ArrowForward,
  Refresh,
  ThumbDown,
  ThumbUp,
} from "@mui/icons-material";
import { Chip, Fab } from "@mui/material";
import Box from "@mui/material/Box";
import {
  motion,
  useAnimation,
  useMotionValue,
  useTransform,
} from "framer-motion";
import React, { useEffect } from "react";
import config from "../config";


export default function HomePage() {
  const x = useMotionValue(0);
  const rotate = useTransform(x, [-190, 190], [-50, 50]);
  const opacity = useTransform(x, [-190, -150, 0, 150, 190], [0, 1, 1, 1, 0]); // Framer animation hook
  const animControls = useAnimation();
  const handleKeyboard = (event: any) => {
    switch(event.key){
      case "ArrowRight":
        animControls.start({ x: 190 })
        break;
      case "ArrowLeft":
        animControls.start({ x: -190 })
        break;
      case "ArrowDown":
        break;
      default:
        break;
    }
  }
  useEffect(()=>{
    document.addEventListener("keydown", handleKeyboard);
  }, [])
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
      <motion.div
        drag="x"
        animate={animControls}
        style={{
          x,
          rotate,
          opacity,
          backgroundImage:
            `url('${config.staticUrl}/Abstract_Brushstroke_Print_Pencil_Skirt/img_00000001.jpg')`,
          backgroundRepeat: "no-repeat",
          backgroundSize: "contain",
          width: 450,
          height: "100%",
          marginTop: "4rem",
          marginBottom: "0.5rem",
        }}
        dragConstraints={{ left: -190, right: 190 }}
        onDragEnd={(event, info) => {
          console.log(info);
          // If the card is dragged only upto 150 on x-axis
          // bring it back to initial position
          if (Math.abs(info.offset.x) <= 150) {
            animControls.start({ x: 0 });
          } else {
            // If card is dragged beyond 150
            // make it disappear
            // making use of ternary operator
            animControls.start({ x: info.offset.x < 0 ? -190 : 190 });
          }
        }}
      />
      <Box
        sx={{
          display: "flex",
          marginBottom: "4rem",
          gap: "1rem",
        }}
      >
        <Fab
          aria-label="dislike"
          color="error"
          onClick={(event) => animControls.start({ x: -190 })}
        >
          <ThumbDown />
        </Fab>
        <Fab aria-label="indiferent">
          <Refresh />
        </Fab>
        <Fab
          aria-label="like"
          color="success"
          onClick={(event) => animControls.start({ x: 190 })}
        >
          <ThumbUp />
        </Fab>
      </Box>
      <Box sx={{ display: "flex", gap: "1rem", marginBottom: "4rem" }}>
        <Chip icon={<ArrowBack />} label="Dislike" />
        <Chip icon={<ArrowDownward />} label="Indiferent" />
        <Chip icon={<ArrowForward />} label="Like" />
      </Box>
    </Box>
  );
}
