import { Send } from "@mui/icons-material";
import {
    Box,
  Divider,
  Fab,
  Grid,
  List,
  ListItem,
  ListItemText,
  TextField,
} from "@mui/material";
import React from "react";

export default function Chat() {


  return (
    <Box sx={{flexGrow: 1, display: "flex", flexDirection: "column" }}>
      <List sx={{ overflowY: "auto", height: "100%", display: "flex", flexDirection: "column" }}>
        <ListItem key="1" sx={{textAlign: "right"}}>
          <Grid container>
            <Grid item xs={12}>
              <ListItemText primary="Hey man, What's up ?"></ListItemText>
            </Grid>
            <Grid item xs={12}>
              <ListItemText secondary="09:30"></ListItemText>
            </Grid>
          </Grid>
        </ListItem>
        <ListItem key="2" sx={{textAlign: "left"}}>
          <Grid container>
            <Grid item xs={12}>
              <ListItemText primary="Hey, Iam Good! What about you ?"></ListItemText>
            </Grid>
            <Grid item xs={12}>
              <ListItemText secondary="09:31"></ListItemText>
            </Grid>
          </Grid>
        </ListItem>
        <ListItem key="3" sx={{textAlign: "right"}}>
          <Grid container>
            <Grid item xs={12}>
              <ListItemText primary="Cool. i am good, let's catch up!"></ListItemText>
            </Grid>
            <Grid item xs={12}>
              <ListItemText secondary="10:30"></ListItemText>
            </Grid>
          </Grid>
        </ListItem>
      </List>
      <Divider />
      <Grid container style={{ padding: "20px" }}>
        <Grid item xs={11}>
          <TextField
            id="outlined-basic-email"
            label="Type Something"
            fullWidth
          />
        </Grid>
        <Grid xs={1}>
          <Fab color="primary" aria-label="add">
            <Send />
          </Fab>
        </Grid>
      </Grid>
    </Box>
  );
}
