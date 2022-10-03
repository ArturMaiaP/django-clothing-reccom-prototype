import { ImageList, Tab, Tabs, Typography } from "@mui/material";
import { Box } from "@mui/system";
import React from "react";
import Chat from "./Chat";
import LikedPhoto from "./LikedPhoto";

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <Box
      sx={{ display: value === index?'flex': 'none', flexGrow: 1 }}
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ p: 3, flexGrow: 1, display: "flex", flexDirection: "column" }}>{children}</Box>}
    </Box>
  );
}

export default function TabMenu() {
  const [value, setValue] = React.useState(0);
  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };
  const data = [
    { name: "img/Abstract_Brushstroke_Print_Pencil_Skirt/img_00000001.jpg" },
    { name: "img/Abstract_Brushstroke_Print_Pencil_Skirt/img_00000002.jpg" },
    { name: "img/Abstract_Brushstroke_Print_Pencil_Skirt/img_00000003.jpg" },
  ];
  return (
    <>
      <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
        <Tabs
          value={value}
          onChange={handleChange}
          aria-label="basic tabs example"
        >
          <Tab label="Likes" aria-controls="likes-tab" />
          <Tab label="Chat" aria-controls="chat-tab" />
        </Tabs>
      </Box>
        <TabPanel value={value} index={0}>
          <ImageList cols={5} sx={{ overflowY: "auto"}}>
            {data.map((item, index) => (
              <LikedPhoto item={item} key={index} />
            ))}
          </ImageList>
        </TabPanel>
        <TabPanel value={value} index={1}>
          <Chat />
        </TabPanel>
    </>
  );
}
