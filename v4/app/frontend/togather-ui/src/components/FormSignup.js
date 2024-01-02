import { Button } from './Button';
import React from 'react';
import useForm from './useForm';
import './Form.css'


const FormSignup = ({ submitForm }) => {
    const { handleChange, handleSubmit, values, errors } = useForm(
        submitForm
  );
    
  return (
    <div className='form-content-right'>
      <form onSubmit={handleSubmit} className='form' noValidate>
        <h1>
          Get started to the easiest way of handling life! Create your account in just few seconds.
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
            type='text'
            name='first_name'
            placeholder='First Name'
            value={values.first_name}
            onChange={handleChange}
          />
          {errors.first_name && <p>{errors.first_name}</p>}
        </div>

        <div className='form-inputs'>
          <input
            className='form-input'
            type='text'
            name='last_name'
            placeholder='Last Name'
            value={values.last_name}
            onChange={handleChange}
          />
          {errors.last_name && <p>{errors.last_name}</p>}
        </div>

        <div className='form-inputs'>
          <input
            className='form-input'
            type='email'
            name='email'
            placeholder='Email'
            value={values.email}
            onChange={handleChange}
          />
          {errors.email && <p>{errors.email}</p>}
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

        <div className='form-inputs'>
          <input
            className='form-input'
            type='password'
            name='password2'
            placeholder='Confirm password'
            value={values.password2}
            onChange={handleChange}
          />
          {errors.password2 && <p>{errors.password2}</p>}
        </div>

        <Button 
        className='form-input-btn'
        type='submit'
        buttonStyle="btn--primary"
        buttonSize="btn--medium"
        >
            Sign Up
        </Button>
        <span className='form-input-login'>
          Already have an account? Login <a href='/login'>here</a>
        </span>
      </form>
    </div>
  );
};

export default FormSignup;