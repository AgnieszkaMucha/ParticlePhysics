import sys  # Import the sys(tem) library for arguments
import ROOT # Import the ROOT library for many uses
 
# Check that the user gave the correct number of arguments
if len(sys.argv) != 3: 
    # Wrong number of arguments, tell the user what you expected
    # Note that sys.argv[0] is how the user called the python script
    print "USAGE: %s <input histogram file> <output plot file>"%(sys.argv[0])
    # End the program
    sys.exit(1)

# Store the user arguments
histFileName = sys.argv[1]
plotFileName = sys.argv[2]

# Retrieve the histograms from the file
# Open the file in read-only mode
histFile  = ROOT.TFile.Open(histFileName,"READ")
# Get the data histogram
dataHisto = histFile.Get("data")
# Get the MC histogram
mcHisto   = histFile.Get("MC")
# Make sure you got the histograms
if not dataHisto:
    print "Failed to get data histogram from the input file"
    sys.exit(1)
if not mcHisto:
    print "Failed to get MC histogram from the input file"
    sys.exit(1)
# Set the histograms to continue to exist after closing the file
dataHisto.SetDirectory(0)
mcHisto.SetDirectory(0)
# Close the input histogram file
histFile.Close()


# Basic style
# Turn off the statistics box
mcHisto.SetStats(0)
dataHisto.SetStats(0)
# Set the line color to red for MC and black for data
mcHisto.SetLineColor(ROOT.kRed)
dataHisto.SetLineColor(ROOT.kBlack)
# Set the line width to 2 for MC and data
mcHisto.SetLineWidth(2)
dataHisto.SetLineWidth(2)
# Set axis labels
mcHisto.GetYaxis().SetTitle("Number of events")
dataHisto.GetYaxis().SetTitle("Number of events")
mcHisto.GetXaxis().SetTitle("m_{ll} [MeV]")
dataHisto.GetXaxis().SetTitle("m_{ll} [MeV]")


# Prepare the canvas for plotting
# Make a canvas
canvas = ROOT.TCanvas("canvas")
# Move into the canvas (so anything drawn is part of this canvas)
canvas.cd()
# Set the y-axis to be logarithmic
canvas.SetLogy(True)


# Open the canvas for continuous printing
# This works for a few file types, most notably pdf files
# This allows you to put several plots in the same pdf file
# The key is the opening square-bracket after the desired file name
canvas.Print(plotFileName+"[")

# Draw the MC histogram, as a Histogram (solid lines)
mcHisto.Draw("h")
# Write the MC histogram plot to the output file
canvas.Print(plotFileName)

# Draw the data histogram, as data Points with Errors
dataHisto.Draw("pe")
# Write the data histogram plot to the output file
canvas.Print(plotFileName)

# The two plots seem to have the same shape, but the y-axis is very different
# The MC needs to be normalized to the data
# The reason is that the MC cross-section has not been used in the weights
# (Normally you would do this, but here we don't know the correspondng MC cross-section)
# As such, we will normalize the MC histogram to have the same number of events as data
mcHisto.Scale(dataHisto.Integral()/mcHisto.Integral())
# Now draw the MC histogram
mcHisto.Draw("h")
# Now draw the data points on the same plot
dataHisto.Draw("pe,same")
# Now write this plot with both the MC and data to the output file
canvas.Print(plotFileName)


# The MC and data agree reasonably well
# Let's plot their ratio to get a better feeling for their agreement
# This is done using a pair of "pads" on the same "canvas"
# For a much more advanced ratio plot, see:
#   https://root.cern.ch/root/html/tutorials/hist/ratioplot.C.html

# Calculate the ratio
# First clone the current data points
ratio = dataHisto.Clone()
# Divide the data points by the MC histogram
ratio.Divide(mcHisto)
# Set the line colour to be red to stand out
ratio.SetLineColor(ROOT.kRed)

# Draw the normal plots (not the ratio)
pad1 = ROOT.TPad("pad1","pad1",0,0.3,1,1)
pad1.SetLogy(True)                      # Set the y-axis of the top plot to be logarithmic
pad1.SetBottomMargin(0)                 # Upper and lower pads are joined
pad1.Draw()                             # Draw the upper pad in the canvas
pad1.cd()                               # pad1 becomes the current pad
mcHisto.SetTitle("")                    # Remove the plot title
mcHisto.GetXaxis().SetLabelSize(0)      # Remove x-axis labels for the top pad
mcHisto.GetXaxis().SetTitleSize(0)      # Remove x-axis title for the top pad
mcHisto.GetYaxis().SetTitleSize(0.05)   # Increase y-axis title size (pad is not full page)
mcHisto.Draw("h")                       # Draw the MC histo in the current pad
dataHisto.Draw("pe,same")               # Draw the data points on top of the MC histo

# Add a legend to the top pad
legend = ROOT.TLegend(0.7,0.6,0.85,0.75)    # Add a legend near the top right corner
legend.AddEntry(mcHisto,"MC")               # Add the MC histogram, labelled as "MC"
legend.AddEntry(dataHisto,"Data")           # Add the data points, labelled as "Data"
legend.SetLineWidth(0)                      # Remove the boundary on the legend
legend.Draw("same")                         # Draw the legend on the plot

# Add other labels with TLatex
# Note that TLatex is global, not pad-related
# As such, the percent-based coordinates for TLatex and the above legend are not the same
latex = ROOT.TLatex()                       # Create the TLatex object
latex.SetNDC()                              # Set the coordinates to be percent-based
latex.SetTextSize(0.06)                     # Increase the text size
latex.DrawText(0.7,0.83,"HASCO 2018")       # Write a label for HASCO
latex.SetTextSize(0.04)                     # Reduce the text size
latex.DrawText(0.7,0.77,"Di-muon events")   # Add a label for the selection

# Now draw the ratio
canvas.cd()                             # Go back to the main canvas before defining pad2
pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.3)
pad2.SetTopMargin(0)                    # Upper and lower pads are joined
pad2.SetBottomMargin(0.25)              # Expand the bottom margin for extra label space
pad2.Draw()                             # Draw the lower pad in the canvas
pad2.cd()                               # pad2 becomes the current pad
ratio.SetTitle("")                      # Turn off the title to avoid overlap
ratio.GetXaxis().SetLabelSize(0.12)     # Larger x-axis labels (pad is not full page)
ratio.GetXaxis().SetTitleSize(0.12)     # Larger x-axis title (pad is not full page)
ratio.GetYaxis().SetLabelSize(0.1)      # Larger y-axis labels (pad is not full page)
ratio.GetYaxis().SetTitleSize(0.15)     # Larger y-axis title (pad is not full page)
ratio.GetYaxis().SetTitle("Data/MC")    # Change the y-axis title (this is the ratio)
ratio.GetYaxis().SetTitleOffset(0.3)    # Reduce the y-axis title spacing
ratio.GetYaxis().SetRangeUser(0.5,1.5)  # Set the y-axis ratio range from 0.5 to 1.5
ratio.GetYaxis().SetNdivisions(207)     # Change the y-axis tick-marks to work better
ratio.Draw("pe")                        # Draw the ratio in the current pad

# Add a line at 1 to the ratio plot
line = ROOT.TLine(50.e3,1,200.e3,1) # Draw a line at 1 from 50 GeV to 200 GeV (full plot)
line.SetLineColor(ROOT.kBlack)      # Set the line colour to black
line.SetLineWidth(2)                # Set the line width to 2
line.Draw("same")                   # Draw the line on the same plot as the ratio

# Write the ratio plot to the output plot file
canvas.Print(plotFileName)

# We're done adding additional plots to the output file
# Close the output file
# The key is the closing square-bracket after the desired file name
canvas.Print(plotFileName + "]")


