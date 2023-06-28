import "./App.css";
import React, { useState } from "react";
import axios from "axios";
import { useForm, Controller } from "react-hook-form";
import { createTheme, ThemeProvider } from "@material-ui/core/styles";
import { LinearProgress, Slider } from "@material-ui/core";

function App() {
  const [price, setPrice] = useState(0);
  const [loading, setLoading] = useState(false);
  const { register, handleSubmit, control } = useForm();

  const onSubmit = (data) => {
    setLoading(true);
    console.log(JSON.stringify(data));
    axios
      .post(
        "https://flight-fare-backend-oln6m6cm6a-uc.a.run.app/api",
        JSON.stringify(data)
      )
      .then((response) => {
        setPrice(response.data["price"]);
        setLoading(false);
        console.log("SUCCESS", response);
      })
      .catch((error) => {
        setLoading(false);
        console.log(error);
      });
  };

  const muiTheme = createTheme({
    palette: {
      secondary: {
        main: "#FFC0CB",
      },
    },
    overrides: {
      MuiSlider: {
        root: {
          color: "#FF7276",
          height: 8,
          "&$vertical": {
            width: 8,
          },
        },
        thumb: {
          height: 24,
          width: 24,
          backgroundColor: "#fff",
          border: "2px solid currentColor",
          marginTop: -8,
          marginLeft: -12,
          "&:focus, &:hover": {
            boxShadow: "0px 0px 0px 8px rgba(84, 199, 97, 0.16)",
          },
          "&$active": {
            boxShadow: "0px 0px 0px 12px rgba(84, 199, 97, 0.16)",
          },
        },
        active: {},
        valueLabel: {
          left: "calc(-50% + 4px)",
        },
        track: {
          height: 8,
          borderRadius: 4,
        },
        rail: {
          height: 8,
          borderRadius: 4,
        },
        vertical: {
          "& $rail": {
            width: 8,
          },
          "& $track": {
            width: 8,
          },
          "& $thumb": {
            marginLeft: -8,
            marginBottom: -11,
          },
        },
      },
    },
  });

  return (
    <div className="App">
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>Airline</label>
        <select {...register("airline", { required: true })}>
          <option value="SpiceJet">SpiceJet</option>
          <option value="AirAsia">AirAsia</option>
          <option value="Vistara">Vistara</option>
          <option value="Air_India">Air_India</option>
          <option value="Indigo">Indigo</option>
          <option value="GO_FIRST">GO_FIRST</option>
        </select>

        <label>Starting City</label>
        <select {...register("source_city", { required: true })}>
          <option value="Delhi">Delhi</option>
          <option value="Mumbai">Mumbai</option>
          <option value="Bangalore">Bangalore</option>
          <option value="Kolkata">Kolkata</option>
          <option value="Hyderabad">Hyderabad</option>
        </select>

        <label>Departure Time</label>
        <select {...register("departure_time", { required: true })}>
          <option value="Early_Morning">Early Morning</option>
          <option value="Morning">Morning</option>
          <option value="Afternoon">Afternoon</option>
          <option value="Evening">Evening</option>
          <option value="Night">Night</option>
        </select>

        <label>Number of Stops</label>
        <Controller
          name="stops"
          control={control}
          defaultValue={0}
          render={({ field }) => (
            <ThemeProvider theme={muiTheme}>
              <Slider
                {...field}
                onChange={(_, value) => {
                  field.onChange(value);
                }}
                valueLabelDisplay="auto"
                marks
                max={5}
                step={1}
              />
            </ThemeProvider>
          )}
        />

        <label>Arrival Time</label>
        <select {...register("arrival_time", { required: true })}>
          <option value="Early_Morning">Early Morning</option>
          <option value="Morning">Morning</option>
          <option value="Afternoon">Afternoon</option>
          <option value="Evening">Evening</option>
          <option value="Night">Night</option>
        </select>

        <label>Destination City</label>
        <select {...register("destination_city", { required: true })}>
          <option value="Delhi">Delhi</option>
          <option value="Mumbai">Mumbai</option>
          <option value="Bangalore">Bangalore</option>
          <option value="Kolkata">Kolkata</option>
          <option value="Hyderabad">Hyderabad</option>
        </select>

        <label>Ticket Class</label>
        <select {...register("class", { required: true })}>
          <option value="Economy">Economy</option>
          <option value="Business">Business</option>
        </select>

        <label>Flight Duration in Hours</label>
        <Controller
          name="duration"
          control={control}
          defaultValue={1}
          render={({ field }) => (
            <ThemeProvider theme={muiTheme}>
              <Slider
                {...field}
                onChange={(_, value) => {
                  field.onChange(value);
                }}
                valueLabelDisplay="auto"
                min={1}
                step={0.01}
                max={50}
              />
            </ThemeProvider>
          )}
        />

        <label>How many days are left until your flight?</label>
        <Controller
          name="days_left"
          control={control}
          defaultValue={1}
          render={({ field }) => (
            <ThemeProvider theme={muiTheme}>
              <Slider
                {...field}
                onChange={(_, value) => {
                  field.onChange(value);
                }}
                valueLabelDisplay="auto"
                min={1}
                step={1}
                max={50}
              />
            </ThemeProvider>
          )}
        />
        <input type="submit" />
        <ThemeProvider theme={muiTheme}>
          <LinearProgress
            variant={loading ? "indeterminate" : "determinate"}
            color="secondary"
            style={{
              height: "5px",
              marginTop: "1em",
              marginBottom: "-1em",
              backgroundColor: "#e75480",
            }}
          />
        </ThemeProvider>
      </form>
      <div>
        <h1>
          Price: ₹{price.toFixed(2)}, or ${(price * 0.012).toFixed(2)}{" "}
        </h1>
      </div>
    </div>
  );
}

export default App;
