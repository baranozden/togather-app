import { Button } from './Button';
import React from 'react';
import useForm from './useForm';

import './Form.css'


const FormLogin = ({ submitForm }) => {
    const { handleChange, handleSubmit, values, errors } = useForm(
        submitForm
  );
    
  return (
    <div className='form-content-right'>
      <form onSubmit={handleSubmit} className='form' noValidate>
        <h1>
            Login to manage everything about your life!
        </h1>
        <div className='form-inputs'>
          <input
            className='form-input'
            type='text'
            name='username'
            placeholder='Username'
            value={values.username}
            onChange={handleChange}
          />
          {errors.username && <p>{errors.username}</p>}
        </div>
        
        <div className='form-inputs'>
          <input
            className='form-input'
            type='password'
            name='password'
            placeholder='Password'
            value={values.password}
            onChange={handleChange}
          />
          {errors.password && <p>{errors.password}</p>}
        </div>
        
        <Button 
        className='form-input-btn'
        type='submit'
        buttonStyle="btn--primary"
        buttonSize="btn--medium"
        >
            Login
        </Button>
        <span className='form-input-login'>
          Forgot your password? Change <a href='/login'>here</a>
        </span>
      </form>
    </div>
  );
};

export default FormLogin;