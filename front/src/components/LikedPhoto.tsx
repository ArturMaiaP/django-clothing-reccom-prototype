import { Delete } from "@mui/icons-material";
import { Fab, ImageListItem, ImageListItemBar } from "@mui/material";
import React from "react";

export default function LikedPhoto(props: { item: any }) {
  return (
    <ImageListItem>
      <img src={`/static/${props.item.name}`} alt="Skirt" loading="lazy" />
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
