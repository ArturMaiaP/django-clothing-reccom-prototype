import { Delete } from "@mui/icons-material";
import { Fab, ImageListItem, ImageListItemBar } from "@mui/material";
import React from "react";
import config from "../config";

export default function LikedPhoto(props: { item: any }) {
  return (
    <ImageListItem>
      <img src={`${config.staticUrl}/${props.item.name}`} alt="Skirt" loading="lazy" />
      <ImageListItemBar
        sx={{ background: "transparent" }}
        actionIcon={
          <Fab size="small" color="error">
            <Delete />
          </Fab>
        }
      />
    </ImageListItem>
  );
}
