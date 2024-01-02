import { FaRegUser } from 'react-icons/fa';
import { GrGroup, GrLogin, GrLogout  } from "react-icons/gr";
import { IoCalendarOutline, IoLogIn } from 'react-icons/io5';
import { LiaUserFriendsSolid } from "react-icons/lia";
import { MdOutlineExplore, MdOutlineLocalActivity } from 'react-icons/md';
import React from 'react';

export const NavbarData = [
    {
        title: "Calendar",
        path: "/calendar",
        icon: <IoCalendarOutline />,
        cname: "nav-text",
        need_auth: true,
    },

    {
        title: "Browse",
        path: "/browse",
        icon: <MdOutlineExplore />,
        cname: "nav-text",
        need_auth: true,
    },

    {
        title: "Profile",
        path: "/profile",
        icon: <FaRegUser />,
        cname: "nav-text",
        need_auth: true,
    },

    {
        title: "Activities",
        path: "/activity",
        icon: <MdOutlineLocalActivity />,
        cname: "nav-text",
        need_auth: true,
    },

    {
        title: "Friends",
        path: "/friends",
        icon: <LiaUserFriendsSolid />,
        cname: "nav-text",
        need_auth: true,
    },

    {
        title: "Communities",
        path: "/communities",
        icon: <GrGroup />,
        cname: "nav-text",
        need_auth: true,
    },

    {
        title: "Logout",
        path: "/logout",
        icon: <GrLogout />,
        cname: "nav-text",
        need_auth: true,
    }
]