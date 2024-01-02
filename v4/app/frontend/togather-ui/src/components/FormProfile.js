import { Button } from './Button';
import React from 'react';
import useForm from './useForm';
import './Form.css'


const FormProfile = ({ submitForm }) => {
    const { handleChange, handleSubmit, values, errors } = useForm(
        submitForm
  );
    
  return (
    <div className='form-content-right'>
      <form onSubmit={handleSubmit} className='form' noValidate>
        <h1>
          Create your profile to show how awesome you are!
        </h1>

        <div className='form-inputs'>
          <input
            className='form-input'
            type='date'
            name='birthday'
            placeholder='birthday'
            value={values.birthday}
            onChange={handleChange}
          />
          {errors.birthday && <p>{errors.birthday}</p>}
        </div>

        <div className='form-inputs'>
          <input
            className='form-input'
            type='file'
            accept="image/*"
            name='picture'
            placeholder='Profile Picture'
            value={values.picture}
            onChange={handleChange}
          />
          {errors.picture && <p>{errors.picture}</p>}
        </div>

        <div className='form-inputs'>
          <input
            className='form-input'
            type='textarea'
            name='bio'
            placeholder='Bio'
            value={values.bio}
            onChange={handleChange}
          />
          {errors.bio && <p>{errors.bio}</p>}
        </div>

        <div className='form-inputs'>
          <select
          className='form-input'
          name='country'
          placeholder='Country'
          value={values.country}
          onChange={handleChange}>
            <option value="turkey">Turkey</option>
          </select>
          {errors.country && <p>{errors.country}</p>}
        </div>

        <div className='form-inputs'>
          <select
          className='form-input'
          name='city'
          placeholder='City'
          value={values.city}
          onChange={handleChange}>
            <option value="ankara">Ankara</option>
          </select>
          {errors.city && <p>{errors.city}</p>}
        </div>

        <div className='form-inputs'>
          <select
          className='form-input'
          name='interest'
          placeholder='Interest'
          value={values.interest}
          onChange={handleChange}>
            <option value="none">None</option>
            <option value="music">Music</option>
            <option value="theatre">Theatre</option>
            <option value="movies">Movies</option>
            <option value="literacy">Literacy</option>
          </select>
          {errors.interest && <p>{errors.interest}</p>}
        </div>

        <Button 
        className='form-input-btn'
        type='submit'
        buttonStyle="btn--primary"
        buttonSize="btn--medium"
        >
            Update Profile
        </Button>
      </form>
    </div>
  );
};

export default FormProfile;