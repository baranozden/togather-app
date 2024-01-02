import axios from 'axios';
import { Button } from '../components/Button';
import { Calendar, dateFnsLocalizer } from "react-big-calendar";
import DatePicker from "react-datepicker";
import format from "date-fns/format";
import getDay from "date-fns/getDay";
import { Modal } from '../components/TaskModal';
import parse from "date-fns/parse";
import startOfWeek from "date-fns/startOfWeek";
import React, { useCallback, useEffect, useState } from "react";

import "react-big-calendar/lib/css/react-big-calendar.css";
import "react-datepicker/dist/react-datepicker.css";


const locales = {
    "en-US": require("date-fns/locale/en-US")
  }
  const localizer = dateFnsLocalizer({
    format,
    parse,
    startOfWeek,
    getDay,
    locales
  })


function Calendars() {
    const [tasks, setTasks] = useState('')
    useEffect(() => {
      if(localStorage.getItem('access_token') === null){                   
          window.location.href = '/login'
      }
      else{
       (async () => {
         try {
           const {data} = await axios.get(   
                          'http://localhost:8000/api/tasks', {
                           headers: {
                              'Content-Type': 'application/json',
                              'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                           }},
                           {withCredentials: true}
                         );
           setTasks(data);
           
        } catch (e) {
          console.log('not auth')
        }
       })()};
   }, []);

      const [showModal, setShowModal] = useState(false)
      const openModal = () => {
        setShowModal(prev => !prev);
      }

      const eventPropGetter = useCallback(
        (event) => ({
          ...(event.priority.includes('low') && {
            className: 'low-priority',
          }),

          ...(event.priority.includes('medium') && {
            className: 'medium-priority',
          }),

          ...(event.priority.includes('high') && {
            className: 'high-priority',
          }),
        }),
        []
      )

    return (
        <div className='calendars'>
            <h1>Calendar</h1>
            <div className='calendar-btns'>
                <Button
                className="btns"
                buttonStyle="btn--primary"
                buttonSize="btn--medium"
                onClick={openModal}
                >
                    Add Task
                </Button>
                <Modal showModal={showModal} setShowModal={setShowModal}/>
            </div>
            
            <Calendar 
            localizer={localizer} 
            events={tasks} 
            titleAccessor="task_name"
            startAccessor={(event) => { return new Date(event.start_date) }}
            endAccessor={(event) => { return new Date(event.end_date) }}
            style={{height: 500, margin: "50px"}}
            onSelectEvent={openModal}
            eventPropGetter={eventPropGetter}
            />
        </div>
    )
}

export default Calendars;