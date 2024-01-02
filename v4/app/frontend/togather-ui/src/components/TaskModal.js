import { AiOutlineClose } from 'react-icons/ai';
import axios from 'axios';
import { Button } from './Button';
import React from "react";
import useForm from './useForm';
import { useState, useEffect } from 'react';

import './Modal.css'

export const Modal = ({showModal, setShowModal}) => {
    const [values, setValues] = useState({
        task_name: '',
        start_date: '',
        end_date: '',
        task_type: 'manual',
        priority: 'low',
        detailed_info: '',
        place: '',
        reminder: 'none',
        recurrence: 'none'
    });

    const [errors, setErrors] = useState({});

    const handleChange = e => {
        const { name, value } = e.target;
        setValues({
        ...values,
        [name]: value
        });
    };

    async function addTask() {
        setErrors({})
        try {
            const {data} = await axios.post(
                'http://localhost:8000/api/addtask',
                values,
                {headers: {'Content-Type': 'application/json', 'Authorization': `Bearer ${localStorage.getItem('access_token')}`}},
                {withCredentials: true}
            )
            console.log(data)
            window.location.href = '/calendar';
            
        } catch (e) {
            setErrors({
                recurrence: "There are problems with your task :("
            }); 
        }
    };

    return (
        <>
            {showModal ? (
                <div className="modal-bg">
                    <div className="modal-wrapper" showModal={showModal}>
                        <AiOutlineClose 
                        className='modal-close'
                        onClick={() => setShowModal(prev => !prev)}/>
                        <div className="modal-content">
                            <h1>Add a New Task</h1>

                            <div className='form-inputs'>
                                <input
                                    className='form-input'
                                    type='text'
                                    name='task_name'
                                    placeholder='Task Title'
                                    value={values.task_name}
                                    onChange={handleChange}
                                />
                                {errors.task_name && <p>{errors.task_name}</p>}
                            </div>

                            <div className='form-inputs'>
                                <input
                                    className='form-input'
                                    type='datetime-local'
                                    name='start_date'
                                    placeholder='Start Date'
                                    value={values.start_date}
                                    onChange={handleChange}
                                />
                                {errors.start_date && <p>{errors.start_date}</p>}
                            </div>

                            <div className='form-inputs'>
                                <input
                                    className='form-input'
                                    type='datetime-local'
                                    name='end_date'
                                    placeholder='End Date'
                                    value={values.end_date}
                                    onChange={handleChange}
                                />
                                {errors.end_date && <p>{errors.end_date}</p>}
                            </div>

                            <div className='form-inputs'>
                                <select
                                className='form-input'
                                name='task_type'
                                placeholder='Task Type'
                                value={values.task_type}
                                onChange={handleChange}>
                                    <option value="manual">Manual</option>
                                    <option value="automated">Automated</option>
                                </select>
                                {errors.task_type && <p>{errors.task_type}</p>}
                            </div>

                            <div className='form-inputs'>
                                <select
                                className='form-input'
                                name='priority'
                                placeholder='Priority'
                                value={values.priority}
                                onChange={handleChange}>
                                    <option value="low">Low</option>
                                    <option value="medium">Medium</option>
                                    <option value="high">High</option>
                                </select>
                                {errors.priority && <p>{errors.priority}</p>}
                            </div>

                            <div className='form-inputs'>
                                <input
                                    className='form-input'
                                    type='text'
                                    name='detailed_info'
                                    placeholder='Details'
                                    value={values.detailed_info}
                                    onChange={handleChange}
                                />
                                {errors.detailed_info && <p>{errors.detailed_info}</p>}
                            </div>

                            <div className='form-inputs'>
                                <input
                                    className='form-input'
                                    type='text'
                                    name='place'
                                    placeholder='Place'
                                    value={values.place}
                                    onChange={handleChange}
                                />
                                {errors.place && <p>{errors.place}</p>}
                            </div>

                            <div className='form-inputs'>
                                <input
                                    className='form-input'
                                    type='file'
                                    name='attachment'
                                    placeholder='Attachment'
                                    value={values.attachment}
                                    onChange={handleChange}
                                />
                                {errors.attachment && <p>{errors.attachment}</p>}
                            </div>

                            <div className='form-inputs'>
                                <select
                                className='form-input'
                                name='reminder'
                                placeholder='Reminder'
                                value={values.reminder}
                                onChange={handleChange}>
                                    <option value="none">None</option>
                                    <option value="before_15">15 minutes before</option>
                                    <option value="before_30">30 minutes before</option>
                                    <option value="before_1d">1 Day before</option>
                                </select>
                                {errors.reminder && <p>{errors.reminder}</p>}
                            </div>

                            <div className='form-inputs'>
                                <select
                                className='form-input'
                                name='recurrence'
                                placeholder='Recurrence'
                                value={values.recurrence}
                                onChange={handleChange}>
                                    <option value="none">None</option>
                                    <option value="daily">Daily</option>
                                    <option value="weekly">Weekly</option>
                                    <option value="monthly">Monthly</option>
                                </select>
                                {errors.recurrence && <p>{errors.recurrence}</p>}
                            </div>

                            <div className="modal-btns">
                                <Button
                                className="btns"
                                buttonStyle="btn--primary"
                                buttonSize="btn--medium"
                                onClick={addTask}
                                >
                                    Add Task
                                </Button>
                            </div>
                        </div>
                    </div>
                </div>
            ) : null}
        </>
    )
}

export default Modal;